import lupa
from random import randrange

runtime = lupa.LuaRuntime(unpack_returned_tuples=True)

runtime.execute("require('server.globals')")
runtime.execute("require('server.hooks')")
runtime.execute("require('server.commands')")

add_player = runtime.eval('function(player) table.insert(PLAYER_TABLE, player); end;')
can_play_hook = runtime.eval("function(hook) return hooks.can_play(hook) end;")

def load_server_script():
    with open('lua/server.lua', 'r') as file:
        server_script = file.read().replace('\n', '')

        runtime.execute(server_script)

load_server_script()

players = []

def generate_random_player():
    p_id = len(players) + 1
    player = {
        'id': p_id,
        'name': "Player {}".format(p_id),
        'usgn': randrange(10000, 100000),
        'ip': '127.0.0.1',
        'port': randrange(30000, 80000),
        'usgnname': "Player {}".format(p_id),
        'bot': randrange(0, 2),
        'steamid': randrange(0, 100000),
        'steamname': "Player {}".format(p_id),
    }

    players.insert(p_id - 1, player)
    add_player(player)

    if can_play_hook("join"):
        runtime.execute("hooks.join('{}')".format(p_id))

generate_random_player()