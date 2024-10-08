local io = require("io")
local os = require("os")
local tempfile = require("os").tmpname
local log_file

-- Function to initialize the log file
local function init_log()
  log_file = io.open("c_executor_debug.log", "w")
end

-- Function to log messages to file and stderr
local function log(...)
  local args = {...}
  for i = 1, #args do
    args[i] = tostring(args[i])
  end
  local message = table.concat(args, " ")
  if log_file then
    log_file:write(message .. "\n")
    log_file:flush()
  end
  io.stderr:write(message .. "\n")
  io.stderr:flush()
end

-- Helper function to execute C code and return the output
local function execute_c_code(code)
  local temp_file = tempfile() .. ".c"
  log("Temporary C file:", temp_file)
  local source_file, err = io.open(temp_file, "w")
  if not source_file then
    log("Failed to create source file:", err)
    error("Failed to create source file: " .. err)
  end

  source_file:write(code)
  source_file:close()

  local temp_bin = tempfile()
  log("Temporary binary file:", temp_bin)

  local compile_command = "gcc " .. temp_file .. " -o " .. temp_bin .. " 2>&1"
  log("Compile Command:", compile_command)
  local compile_pipe = io.popen(compile_command)
  local compile_output = compile_pipe:read("*a")
  local compile_result = compile_pipe:close()

  if compile_result ~= true then
    os.remove(temp_file)
    log("C compilation failed. Output:", compile_output)
    error("C compilation failed. Output: " .. compile_output)
  end

  local exec_command = temp_bin .. " 2>&1"
  log("Exec Command:", exec_command)
  local exec_pipe = io.popen(exec_command)
  local output = exec_pipe:read("*a")
  exec_pipe:close()

  local ok, rm_err = pcall(function()
    os.remove(temp_file)
    os.remove(temp_bin)
  end)
  if not ok then
    log("Failed to clean up temporary files:", rm_err)
    error("Failed to clean up temporary files: " .. rm_err)
  end

  log("Output:", output)
  return output
end

local echo_global = true

function Meta(meta)
  if meta.echo ~= nil then
    echo_global = pandoc.utils.stringify(meta.echo) == "true"
  end
end

-- Lua filter function
function CodeBlock(elem)
  if not log_file then
    init_log()
  end

  local is_c_code = elem.attr.classes:includes("{c}")
  if is_c_code then
    log("Processing C code block")
    local output = execute_c_code(elem.text)
    output = output:gsub("%s+$", "")
    local blocks = {}

    if echo_global then
      -- Render C code as a formatted block
      table.insert(blocks, pandoc.CodeBlock(elem.text, {class="c"}))
    end

    -- Always return the output
    table.insert(blocks, pandoc.Para(pandoc.Str(output)))

    return blocks
  else
    log("Skipping non-C code block")
  end
end

-- Ensure log file is closed properly at the end
function Pandoc(doc)
  if log_file then
    log_file:close()
  end
  return doc
end

