function player(id, property)
    for v, i in pairs(PLAYER_TABLE) do
        if tostring(v) == tostring(id) then
            return i[property]
        end
    end

    return nil
end
