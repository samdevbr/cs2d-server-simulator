function handle_join(player_id)
    print('Player ID: ' .. player_id)
end;

addhook('join', 'handle_join')
