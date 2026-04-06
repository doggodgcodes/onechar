local chars = io.read()
local asc = 0
local final = ""

print("")
-- Lua port made by Gemini 3
-- In Lua, we iterate through each character using string.gmatch
for character in chars:gmatch(".") do
    if character == "-" then
        asc = asc - 1
    elseif character == "+" then
        asc = asc + 1
    elseif character == "." then
        if asc > 255 then
            asc = asc - 255
        end
        -- string.char converts the byte to a character
        final = final .. string.char(math.floor(asc))
    elseif character == "*" then
        asc = asc * asc
    elseif character == "/" then
        -- Warning: potential division by zero if asc is 0
        asc = asc / asc
    elseif character == "^" then
        asc = asc * asc - asc
    elseif character == "!" then
        print(asc)
    elseif character == ";" then
        asc = asc * 2
    end
end

print(final)
