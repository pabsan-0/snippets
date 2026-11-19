TAG='1.26.8'
shopt -s extglob

COMMITS=()

relevant_commits() {
    cmd=${1-""}
    echo "--- $cmd"
    while read -r  commit __; do
        commit="${commit//$'\e['*([0-9;])[a-zA-Z]/}"

        if [[ -z $( git tag $TAG --contains="$commit" ) ]]; then
            echo "NEED $commit $__"
            COMMITS+=("$commit")
        else
            echo -e "\e[90mDROP $commit $__\e[0m"
            break
        fi
    done < <($cmd)
    echo
}

# Specifically selected commits (from #8679)
COMMITS+=(d9bbfc27fdc991c35070b4588b4f931d228e1a0d)
COMMITS+=(740b7564ee553d642724d46dbf3db12c36e8d975)
COMMITS+=(deee13a6c3e2e3d13a9ed051dadcc461e2d92e2d)
COMMITS+=(1bd5afa460935d3c96b443960676517308ea1bb3)

# Commits affecting X files
relevant_commits "git log --oneline main -- subprojects/gst-plugins-bad/gst/codectimestamper"
relevant_commits "git log --oneline main -- subprojects/gst-plugins-bad/gst/closedcaption/*"
relevant_commits "git log --oneline main -- subprojects/gst-plugins-bad/ext/closedcaption/*"

# Sort by time and print all
if [[ ${#COMMITS[@]} -gt 0 ]]; then
    # Sort from oldest to newest
    sorted_commits=($(git show -s --format="%ct %H" "${COMMITS[@]}" | sort -n | awk '{print $2}'))

    echo "--- reordered commits (older first)"
    final_commits=()
    for commit in "${sorted_commits[@]}"; do
        status=$(git cherry "$TAG" "$commit" "$commit^" | awk '{print $1}')

        if [[ "$status" == "-" ]]; then
            echo -e "\e[90mDROP $commit # already backported\e[0m"
        else
            echo "NEED $commit"
            final_commits+=("$commit")
        fi
    done
else
    echo "No commits collected."
fi

echo
echo
echo
if [[ ${#final_commits[@]} -gt 0 ]]; then
    printf "git cherry-pick -x %s\n" "${final_commits[@]}"
else
    echo "All selected commits have already been backported."
fi
