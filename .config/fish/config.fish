
# ==========================================
# FISH SHELL
# ==========================================

# No greeting
set -g fish_greeting ""

# Default editor
set -gx EDITOR nvim
set -gx VISUAL nvim

# Color support
set -gx TERM xterm-256color
set -gx COLORTERM truecolor

# Colors for Fish autosuggestions
set -g fish_color_autosuggestion brblack
set -g fish_color_command cyan
set -g fish_color_error red
set -g fish_color_param normal
set -g fish_color_quote green
set -g fish_color_comment brblack
set -g fish_color_operator magenta
set -g fish_color_end brmagenta
set -g fish_color_cwd cyan
set -g fish_color_user green
set -g fish_color_host brcyan
set -g fish_color_search_match --background=brblack

# Neon-style prompt
function fish_prompt
    set -l last_status $status

    set_color brcyan
    printf '╭─ '

    set_color brmagenta
    printf '%s' (prompt_pwd)

    set_color normal
    printf '\n'

    if test $last_status -eq 0
        set_color brgreen
        printf '╰─❯ '
    else
        set_color brred
        printf '╰─✗ '
    end

    set_color normal
end


# ==========================================
# FASTFETCH ON KITTY STARTUP
# ==========================================

if status is-interactive
    and set -q KITTY_WINDOW_ID
    fastfetch
end

starship init fish | source

