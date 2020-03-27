hooks = {}

hooks.join = nil
hooks.say = nil

hooks.can_play = function (name)
    return hooks[name] ~= nil
end

function addhook(name, callback)
    hooks[name] = _G[callback]
end
