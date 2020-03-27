import lupa

runtime = lupa.LuaRuntime(unpack_returned_tuples=True)

runtime.execute("require('server.hooks')")

def load_server_script():
    with open('lua/server.lua', 'r') as file:
        server_script = file.read().replace('\n', '')

        runtime.execute(server_script)

load_server_script()

def play_join():
    player_id = 1
    runtime.execute("if hooks.can_play('join') then hooks.join('{}') end;".format(player_id))

play_join()
