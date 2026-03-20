import click
import sys
import os

# 確保 Python 可以找到同目錄下的 task_manager.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from task_manager import TaskManager

tm = TaskManager()

@click.group()
def cli():
    """Maggie's Task Manager CLI v1.0"""
    pass

@cli.command()
@click.option('--title', required=True, help='任務名稱')
def add(title):
    """新增任務指令"""
    task = tm.add_task(title)
    click.echo(f"Task added: [{task['id']}] {task['title']}")

@cli.command()
def list():
    """列出任務指令"""
    tasks = tm.list_tasks()
    if not tasks:
        click.echo("目前沒有任務。")
        return
    click.echo(f"{'ID':<4} {'狀態':<4} {'任務名稱'}")
    click.echo("-" * 30)
    for t in tasks:
        status_icon = "✅" if t['status'] == "done" else "❌"
        click.echo(f"{t['id']:<4} {status_icon:<4} {t['title']}")

@cli.command()
@click.option('--id', type=int, required=True, help='任務 ID')
def done(id):
    """完成任務指令"""
    if tm.mark_done(id):
        click.echo(f"Task {id} marked as done!")
    else:
        click.echo(f"Error: 找不到 ID 為 {id} 的任務", err=True)

if __name__ == '__main__':
    cli()