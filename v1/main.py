import click
import sys
import os

# 解決路徑問題，確保匯入正確
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from task_manager import TaskManager

tm = TaskManager()

@click.group()
def cli():
    """🚀 Maggie's Advanced Task Manager v1.0
    
    這是一個符合 SDD 規格開發的 CLI 工具。
    """
    pass

@cli.command()
@click.option('--title', '-t', required=True, help='任務的標題描述')
def add(title):
    """新增一個待辦任務到清單中"""
    try:
        task = tm.add_task(title)
        click.secho(f"Successfully added Task #{task['id']}: {task['title']}", fg='green')
    except Exception as e:
        click.secho(f"Error: {e}", fg='red', err=True)

@cli.command()
def list():
    """顯示目前所有的任務狀態"""
    tasks = tm.list_tasks()
    if not tasks:
        click.echo("Your task list is currently empty. 🏖️")
        return

    click.echo("\n" + "="*45)
    click.echo(f"{'ID':<5} {'Status':<10} {'Task Title'}")
    click.echo("-" * 45)
    
    for t in tasks:
        color = 'green' if t['status'] == 'done' else 'yellow'
        icon = "✅" if t['status'] == "done" else "⏳"
        status_text = click.style(f"{icon} {t['status']}", fg=color)
        click.echo(f"{t['id']:<5} {status_text:<18} {t['title']}")
    click.echo("="*45 + "\n")

@cli.command()
@click.option('--id', type=int, required=True, help='要完成的任務 ID')
def done(id):
    """將任務標記為完成狀態"""
    if tm.mark_done(id):
        click.secho(f"Task #{id} is now complete! 🌟", fg='cyan')
    else:
        click.secho(f"Error: Task #{id} not found.", fg='red', err=True)

@cli.command()
@click.option('--id', type=int, required=True, help='要刪除的任務 ID')
def delete(id):
    """從清單中永久刪除任務"""
    if tm.delete_task(id):
        click.secho(f"Task #{id} has been deleted.", fg='magenta')
    else:
        click.secho(f"Error: Task #{id} not found.", fg='red', err=True)

if __name__ == '__main__':
    cli()
