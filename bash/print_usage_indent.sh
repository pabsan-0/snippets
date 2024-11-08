print_usage() {
    local source=${BASH_SOURCE[0]}
    local indent=$(printf "%*s" ${#source})   # Adjust the padding to align text nicely

    echo "Usage: ${source}                                                                      "
    echo "       ${indent} [ --dry-run ]            : display generated tmux config and exit    "
    echo "       ${indent} [ --no-kill-session ]    : don't kill tmux session after detach      "
    echo "       ${indent} [ --no-kill-containers ] : don't kill docker containers after detach "
    echo "       ${indent} [ --help ]               : display this help and exit                "
    echo "                                                                                      "
    echo "Launches all services in a docker compose file, each on its own tmux pane.            "
}
