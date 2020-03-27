function handle_join(player_id)
    print(player(player_id, "name"))
    print(player(player_id, "usgn"))
    print(player(player_id, "ip"))
    print("----------------------")
end;

addhook('join', 'handle_join')
