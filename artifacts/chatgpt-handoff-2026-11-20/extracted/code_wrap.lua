function Code(el)
  if FORMAT:match('latex') and (el.text:find('/') or #el.text > 35) then
    return pandoc.RawInline('latex', '\\path{' .. el.text .. '}')
  end
end
