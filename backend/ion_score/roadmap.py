"""`ion repo score --roadmap`: what no converter closes, handed to Claude as a short list.

Most of an agent's tokens go into exploring a repo to find what to do; the roadmap gives it the
places instead, so Claude pays to think, not to search. Each item has its rule, its why, where
to look (file and line) and how to prove it closed (`ion repo score --rule ID`). An approximate
detector's places are candidates "to confirm": Claude confirms or dismisses each in one look,
and a dismissal is a waiver on that path (`ion repo waive ID --paths … --permanent`), never flagged
again. `--write` turns the items into tickets of `docs/backlog/backlog.md`, once each.
"""

import datetime
from pathlib import Path

from ion_score import checks, ui
from ion_score.score import FAILED, Finding, Report
from ion_score.shell import IonError
from ion_score.tickets import NEXT_FREE, ticket_id

BACKLOG = Path("docs") / "backlog" / "backlog.md"
NORMAL_SECTION = "## 🟡 Normal"
SHOWN_LOCATIONS = 5
FALSE_POSITIVE = 'ion repo waive {rule} --paths <file> --permanent --reason "false positive: …"'


def screen(report: Report) -> list[str]:
    items = report.roadmap()
    lines: list[str] = []
    title = ui.paint("ion-repo roadmap", ui.FIRE, bold=True)
    lines.append(f"\n  {title}  {ui.paint(f'{len(items)} gap(s) for Claude', ui.GLOW, bold=True)}")
    if not items:
        scripted = sum(found.by_script for found in report.gaps)
        rest = f"; {scripted} closed by script: ion repo fix" if scripted else ""
        lines.append(ui.paint(f"  Nothing that needs judgment{rest}.", ui.STONE))
        return lines
    lines.append(ui.paint("  Sure gaps first, then the smallest; each one +1 rule met.", ui.STONE))
    logs = checks.reverted(Path(report.root)) if report.reverted else {}
    for number, found in enumerate(items, 1):
        mark = ui.paint("  to confirm", ui.FIRE) if found.confirm else ""
        lines.append(
            f"\n  {number}. {ui.paint(found.rule, ui.EMBER, bold=True)}  {found.title}{mark}"
        )
        lines.append(ui.paint(f"     why: {found.why}", ui.STONE_LIGHT))
        for location in found.locations[:SHOWN_LOCATIONS]:
            lines.append(ui.paint(f"     {location}", ui.STONE))
        if (more := len(found.locations) - SHOWN_LOCATIONS) > 0:
            lines.append(
                ui.paint(f"     … and {more} more (ion repo score --rule {found.rule})", ui.STONE)
            )
        if found.detail:
            lines.append(ui.paint(f"     {found.detail}", ui.STONE))
        if log := logs.get(found.rule):
            lines.append(
                ui.paint(f"     ion repo fix's commit broke a check, set aside: {log}", ui.STONE)
            )
        lines.append(ui.paint(f"     done when: ion repo score --rule {found.rule}", ui.STONE))
    lines.append(ui.paint("\n  One at a time with Claude Code: /repo:modernize", ui.STONE))
    lines.append(ui.paint(f"  A false positive: {FALSE_POSITIVE.format(rule='<ID>')}", ui.STONE))
    return lines


def rule_screen(found: Finding | None, rule_id: str) -> list[str]:
    """`--rule ID`: the proof that a gap is closed, its places while it is open (`is_open`)."""
    if found is None:
        raise IonError(f"{rule_id}: not scored in this repo (unknown, or not for its stacks)")
    if not is_open(found):
        return [f"\n{ui.paint('✓', ui.MOSS, bold=True)} {rule_id}: {found.status}, {found.title}"]
    lines: list[str] = []
    lines.append(f"\n  {ui.paint(rule_id, ui.EMBER, bold=True)}  {found.title}")
    for location in found.locations:
        lines.append(ui.paint(f"    {location}", ui.STONE))
    if found.detail:
        lines.append(ui.paint(f"    {found.detail}", ui.STONE))
    return lines


def is_open(found: Finding) -> bool:
    return found.status == FAILED


def still_open(found: Finding) -> IonError:
    return IonError(f"{found.rule} still open ({len(found.locations) or 1} place(s))")


def write_tickets(root: Path, report: Report, today: datetime.date | None = None) -> list[str]:
    """One ticket per roadmap item not tracked yet, under 🟡 Normal; returns their IDs."""
    path = root / BACKLOG
    if not path.exists():
        raise IonError(f"no {BACKLOG} in this repo: ion repo adopt sets it up")
    text = path.read_text()
    match = NEXT_FREE.search(text)
    if match is None or NORMAL_SECTION not in text:
        raise IonError(f"{BACKLOG}: no 'Next free: <repo>#T-NN' or no '{NORMAL_SECTION}' section")
    number = int(match.group(1))
    day = (today or datetime.date.today()).isoformat()
    written, tickets = [], []
    for found in report.roadmap():
        if _marker(found.rule) in text:
            continue
        tickets.append(_ticket(ticket_id(root, number), found, day))
        written.append(ticket_id(root, number))
        number += 1
    if not tickets:
        return []
    text = NEXT_FREE.sub(f"Next free: {ticket_id(root, number)}", text, count=1)
    text = text.replace(NORMAL_SECTION, NORMAL_SECTION + "\n\n" + "\n\n".join(tickets), 1)
    path.write_text(text)
    return written


def _marker(rule_id: str) -> str:
    return f"grid rule `{rule_id}`"


def _ticket(written_id: str, found: Finding, day: str) -> str:
    where = "\n".join(f"- [ ] `{location}`" for location in found.locations)
    confirm = " Candidates to confirm: a false positive is dismissed by a waiver." * found.confirm
    lines = [
        f"### {written_id} · {found.title}",
        "- **Type**: improvement",
        "- **Status**: todo",
        f"- **Opened**: {day}",
        "- **Effort**: S · **Owner**: — · **Due**: —",
        f"- **Origin**: ion repo score --roadmap, {_marker(found.rule)}",
        "",
        f"{found.why}{confirm} Source: {found.source}. Done when `ion repo score --rule "
        f"{found.rule}` "
        "passes and the checks stay green (`/repo:modernize`).",
    ]
    if where:
        lines += ["", where]
    return "\n".join(lines)
