import click
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from task_manager import TaskManager

tm = TaskManager()

@click.group()
def cli():
    """🚀 Maggie's Task Master v2.0 - Enhanced Edition"""
    pass

@cli.command()
@click.option('--title', '-t', required=True, help='任務名稱')
@click.option('--priority', '-p', type=click.Choice(['High', 'Medium', 'Low']), default='Medium', help='優先級 (預設 Medium)')
def add(title, priority):
    task = tm.add_task(title, priority)
    click.secho(f"✅ Task Added: [{task['id']}] {task['title']} ({task['priority']})", fg='green')

@cli.command()
@click.option('--status', '-s', type=click.Choice(['todo', 'done']), help='篩選狀態')
def list(status):
    tasks = tm.list_tasks(status)
    if not tasks:
        click.echo("📭 No tasks found matching the criteria.")
        return
    
    click.echo(f"{'ID':<4} {'Status':<8} {'Prio':<8} {'Title'}")
    click.echo("-" * 40)
    for t in tasks:
        icon = "✅" if t['status'] == "done" else "⏳"
        prio_color = 'red' if t['priority'] == 'High' else 'yellow' if t['priority'] == 'Medium' else 'blue'
        prio_text = click.style(f"{t['priority']:<8}", fg=prio_color)
        click.echo(f"{t['id']:<4} {icon} {t['status']:<6} {prio_text} {t['title']}")

@cli.command()
@click.option('--id', type=int, required=True)
def delete(id):
    task = tm.get_task_by_id(id)
    if not task:
        click.secho(f"❌ Error: Task {id} not found.", fg='red')
        return
    
    # 需求 3: 互動式確認
    if click.confirm(f"⚠️ Are you sure you want to delete Task: '{task['title']}'?", abort=True):
        tm.delete_task(id)
        click.secho(f"🗑️ Task {id} deleted.", fg='magenta')

@cli.command()
@click.option('--id', type=int, required=True)
@click.option('--title', '-t', help='新的標題')
@click.option('--priority', '-p', type=click.Choice(['High', 'Medium', 'Low']), help='新的優先級')
def edit(id, title, priority):
    if not title and not priority:
        click.echo("Please provide at least one field to update (--title or --priority).")
        return
        
    if tm.edit_task(id, title, priority):
        click.secho(f"📝 Task {id} updated successfully.", fg='cyan')
    else:
        click.secho(f"❌ Error: Task {id} not found.", fg='red')

@cli.command()
@click.option('--id', type=int, required=True)
def done(id):
    if tm.mark_done(id):
        click.secho(f"🌟 Task {id} marked as done!", fg='yellow')
    else:
        click.secho(f"❌ Error: Task {id} not found.", fg='red')

if __name__ == '__main__':
    cli()