TILE_LIST = [
    "1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m",
    "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
    "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s",
    "E",  "S",  "W",  "N",  "P",  "F",  "C", 
    "5mr", "5pr", "5sr"
]

TILE_2_UNICODE = {
    '5mr':'🀋',
    '1m': '🀇',
    '2m': '🀈',
    '3m': '🀉',
    '4m': '🀊',
    '5m': '🀋',
    '6m': '🀌',
    '7m': '🀍',
    '8m': '🀎',
    '9m': '🀏',
    '5pr':'🀝',
    '1p': '🀙',
    '2p': '🀚',
    '3p': '🀛',
    '4p': '🀜',
    '5p': '🀝',
    '6p': '🀞',
    '7p': '🀟',
    '8p': '🀠',
    '9p': '🀡',
    '5sr':'🀔',
    '1s': '🀐',
    '2s': '🀑',
    '3s': '🀒',
    '4s': '🀓',
    '5s': '🀔',
    '6s': '🀕',
    '7s': '🀖',
    '8s': '🀗',
    '9s': '🀘',
    '1z': '🀀',
    '2z': '🀁',
    '3z': '🀂',
    '4z': '🀃',
    '5z': '🀆',
    '6z': '🀅',
    '7z': '🀄',
    # '?': '🀫',
    '?': '',
    'E': '🀀',
    'S': '🀁',
    'W': '🀂',
    'N': '🀃',
    'P': '🀆',
    'F': '🀅',
    'C': '🀄',
}

TILE_2_UNICODE_ART = {
    '5mr': 
    """╭──────╮
│ .伍  │
│      │
│  萬  │
╰──────╯""",
    '1m': 
    """╭──────╮
│  一  │
│      │
│  萬  │
╰──────╯""",
    '2m': 
    """╭──────╮
│  二  │
│      │
│  萬  │
╰──────╯""",
    '3m': 
    """╭──────╮
│  三  │
│      │
│  萬  │
╰──────╯""",
    '4m': 
    """╭──────╮
│  四  │
│      │
│  萬  │
╰──────╯""",
    '5m': 
    """╭──────╮
│  伍  │
│      │
│  萬  │
╰──────╯""",
    '6m': 
    """╭──────╮
│  六  │
│      │
│  萬  │
╰──────╯""",
    '7m': 
    """╭──────╮
│  七  │
│      │
│  萬  │
╰──────╯""",
    '8m': 
    """╭──────╮
│  八  │
│      │
│  萬  │
╰──────╯""",
    '9m': 
    """╭──────╮
│  九  │
│      │
│  萬  │
╰──────╯""",
    '5pr': 
    """╭─────╮
│ ● ● │
│ .●  │
│ ● ● │
╰─────╯""",
    '1p': 
    """╭─────╮
│     │
│  ●  │
│     │
╰─────╯""",
    '2p': 
    """╭─────╮
│  ●  │
│     │
│  ●  │
╰─────╯""",
    '3p': 
    """╭─────╮
│ ●   │
│  ●  │
│   ● │
╰─────╯""",
    '4p': 
    """╭─────╮
│ ● ● │
│     │
│ ● ● │
╰─────╯""",
    '5p': 
    """╭─────╮
│ ● ● │
│  ●  │
│ ● ● │
╰─────╯""",
    '6p': 
    """╭─────╮
│ ● ● │
│ ● ● │
│ ● ● │
╰─────╯""",
    '7p': 
    """╭─────╮
│● ● ●│
│ ● ● │
│ ● ● │
╰─────╯""",
    '8p': 
    """╭─────╮
│ 8 8 │
│ ● ● │
│ ● ● │
╰─────╯""",
    '9p': 
    """╭─────╮
│● ● ●│
│● ● ●│
│● ● ●│
╰─────╯""",
    '5sr': 
    """╭─────╮
│ I.I │
│  I  │
│ I I │
╰─────╯""",
    '1s': 
    """╭─────╮
│  ╦  │
│  ║  │
│  ╩  │
╰─────╯""",
    '2s': 
    """╭─────╮
│  I  │
│     │
│  I  │
╰─────╯""",
    '3s': 
    """╭─────╮
│  I  │
│     │
│ I I │
╰─────╯""",
    '4s': 
    """╭─────╮
│ I I │
│     │
│ I I │
╰─────╯""",
    '5s': 
    """╭─────╮
│ I I │
│  I  │
│ I I │
╰─────╯""",
    '6s': 
    """╭─────╮
│ I I │
│ I I │
│ I I │
╰─────╯""",
    '7s': 
    """╭─────╮
│  I  │
│I I I│
│I I I│
╰─────╯""",
    '8s': 
    """╭─────╮
││╱ ╲││
│     │
││╲ ╱││
╰─────╯""",
    '9s': 
    """╭─────╮
│I I I│
│I I I│
│I I I│
╰─────╯""",
    'E': 
    """╭──────╮
│      │
│  東  │
│      │
╰──────╯""",
    'S': 
    """╭──────╮
│      │
│  南  │
│      │
╰──────╯""",
    'W': 
    """╭──────╮
│      │
│  西  │
│      │
╰──────╯""",
    'N': 
    """╭──────╮
│      │
│  北  │
│      │
╰──────╯""",
    'P': 
    """╭──────╮
│      │
│      │
│      │
╰──────╯""",
    'F': 
    """╭──────╮
│      │
│  發  │
│      │
╰──────╯""",
    'C': 
    """╭──────╮
│      │
│  中  │
│      │
╰──────╯""",
}

TILE_2_UNICODE_ART_RICH = {
    '5mr': 
    """[bold red]╭──────╮
│ .伍  │
│      │
│  萬  │
╰──────╯""",
    '1m': 
    """[bold]╭──────╮
│  一  │
│      │
│  [red]萬[/red]  │
╰──────╯""",
    '2m': 
    """[bold]╭──────╮
│  二  │
│      │
│  [red]萬[/red]  │
╰──────╯""",
    '3m': 
    """[bold]╭──────╮
│  三  │
│      │
│  [red]萬[/red]  │
╰──────╯""",
    '4m': 
    """[bold]╭──────╮
│  四  │
│      │
│  [red]萬[/red]  │
╰──────╯""",
    '5m': 
    """[bold]╭──────╮
│  伍  │
│      │
│  [red]萬[/red]  │
╰──────╯""",
    '6m': 
    """[bold]╭──────╮
│  六  │
│      │
│  [red]萬[/red]  │
╰──────╯""",
    '7m': 
    """[bold]╭──────╮
│  七  │
│      │
│  [red]萬[/red]  │
╰──────╯""",
    '8m': 
    """[bold]╭──────╮
│  八  │
│      │
│  [red]萬[/red]  │
╰──────╯""",
    '9m': 
    """[bold]╭──────╮
│  九  │
│      │
│  [red]萬[/red]  │
╰──────╯""",
    '5pr': 
    """[bold red]╭─────╮
│ ● ● │
│ .●  │
│ ● ● │
╰─────╯""",
    '1p': 
    """[bold]╭─────╮
│     │
│  ●  │
│     │
╰─────╯""",
    '2p': 
    """[bold]╭─────╮
│  ●  │
│     │
│  ●  │
╰─────╯""",
    '3p': 
    """[bold]╭─────╮
│ ●   │
│  [red]●[/red]  │
│   ● │
╰─────╯""",
    '4p': 
    """[bold]╭─────╮
│ ● ● │
│     │
│ ● ● │
╰─────╯""",
    '5p': 
    """[bold]╭─────╮
│ ● ● │
│  [red]●[/red]  │
│ ● ● │
╰─────╯""",
    '6p': 
    """[bold]╭─────╮
│ ● ● │
│ [red]● ●[/red] │
│ [red]● ●[/red] │
╰─────╯""",
    '7p': 
    """[bold]╭─────╮
│● ● ●│
│ [red]● ●[/red] │
│ [red]● ●[/red] │
╰─────╯""",
    '8p': 
    """[bold]╭─────╮
│ 8 8 │
│ ● ● │
│ ● ● │
╰─────╯""",
    '9p': 
    """[bold]╭─────╮
│● ● ●│
│[red]● ● ●[/red]│
│● ● ●│
╰─────╯""",
    '5sr': 
    """[bold red]╭─────╮
│ I.I │
│  I  │
│ I I │
╰─────╯""",
    '1s': 
    """[bold]╭─────╮
│  [green]╦[/green]  │
│  [green]║[/green]  │
│  [green]╩[/green]  │
╰─────╯""",
    '2s': 
    """[bold]╭─────╮
│  [green]I[/green]  │
│     │
│  [green]I[/green]  │
╰─────╯""",
    '3s': 
    """[bold]╭─────╮
│  [green]I[/green]  │
│     │
│ [green]I I[/green] │
╰─────╯""",
    '4s': 
    """[bold]╭─────╮
│ [green]I I[/green] │
│     │
│ [green]I I[/green] │
╰─────╯""",
    '5s': 
    """[bold]╭─────╮
│ [green]I I[/green] │
│  [red]I[/red]  │
│ [green]I I[/green] │
╰─────╯""",
    '6s': 
    """[bold]╭─────╮
│ [green]I I[/green] │
│ [green]I I[/green] │
│ [green]I I[/green] │
╰─────╯""",
    '7s': 
    """[bold]╭─────╮
│  [red]I[/red]  │
│[green]I I I[/green]│
│[green]I I I[/green]│
╰─────╯""",
    '8s': 
    """[bold]╭─────╮
│[green]│╱ ╲│[/green]│
│     │
│[green]│╲ ╱│[/green]│
╰─────╯""",
    '9s': 
    """[bold]╭─────╮
│[green]I[/green] [red]I[/red] [green]I[/green]│
│[green]I[/green] [red]I[/red] [green]I[/green]│
│[green]I[/green] [red]I[/red] [green]I[/green]│
╰─────╯""",
    'E': 
    """[bold]╭──────╮
│      │
│  東  │
│      │
╰──────╯""",
    'S': 
    """[bold]╭──────╮
│      │
│  南  │
│      │
╰──────╯""",
    'W': 
    """[bold]╭──────╮
│      │
│  西  │
│      │
╰──────╯""",
    'N': 
    """[bold]╭──────╮
│      │
│  北  │
│      │
╰──────╯""",
    'P': 
    """[bold]╭──────╮
│      │
│      │
│      │
╰──────╯""",
    'F': 
    """[bold]╭──────╮
│      │
│  [green]發[/green]  │
│      │
╰──────╯""",
    'C': 
    """[bold]╭──────╮
│      │
│  [red]中[/red]  │
│      │
╰──────╯""",
    '?': 
#     """[bold]╭─────╮
# │ ┏━┓ │
# │  ┏┛ │
# │  ●  │
# ╰─────╯""",
    """[bold]       
       
       
       
       """,

}

VERTICAL_RULE = """║
║
║
║
║"""

EMPTY_VERTICAL_RULE = """ 
 
 
 
 """

#▁▂▃▄▅▆▇█
HAI_VALUE = [
'[red]\n \n \n \n▁',
'[red]\n \n \n \n▂',
'[red]\n \n \n \n▃',
'[red]\n \n \n \n▄',        # ~ 10%
'[yellow]\n \n \n \n▅',
'[yellow]\n \n \n \n▆',
'[yellow]\n \n \n \n▇',
'[yellow]\n \n \n \n█',     # ~ 20%
'[yellow]\n \n \n▁\n█',
'[yellow]\n \n \n▂\n█',
'[yellow]\n \n \n▃\n█',
'[yellow]\n \n \n▄\n█',     # ~ 30%
'[yellow]\n \n \n▅\n█',
'[yellow]\n \n \n▆\n█',
'[yellow]\n \n \n▇\n█',
'[yellow]\n \n \n█\n█',     # ~ 40%
'[green]\n \n▁\n█\n█',
'[green]\n \n▂\n█\n█',
'[green]\n \n▃\n█\n█',
'[green]\n \n▄\n█\n█',      # ~ 50%
'[green]\n \n▅\n█\n█',
'[green]\n \n▆\n█\n█',
'[green]\n \n▇\n█\n█',
'[green]\n \n█\n█\n█',      # ~ 60%
'[green]\n▁\n█\n█\n█',
'[green]\n▂\n█\n█\n█',
'[green]\n▃\n█\n█\n█',
'[green]\n▄\n█\n█\n█',      # ~ 70%
'[green]\n▅\n█\n█\n█',
'[green]\n▆\n█\n█\n█',
'[green]\n▇\n█\n█\n█',
'[green]\n█\n█\n█\n█',      # ~ 80%
'[blue]▁\n█\n█\n█\n█',
'[blue]▂\n█\n█\n█\n█',
'[blue]▃\n█\n█\n█\n█',
'[blue]▄\n█\n█\n█\n█',     # ~ 90%
'[blue]▅\n█\n█\n█\n█',
'[blue]▆\n█\n█\n█\n█',
'[blue]▇\n█\n█\n█\n█',
'[blue]█\n█\n█\n█\n█',     # ~ 100%
''                         # none
]