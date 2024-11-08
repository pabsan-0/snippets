executable_exists() {
    if command -v $1 2>&1 >/dev/null; then
        return 0
    else
        echo "[INFO] Command '$1' could not be found"
        return 1
    fi
}
