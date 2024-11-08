local arg__foo=false
local arg__bar=false

while ((${#}))
do
    local arg="${1:-}"
    echo $arg

    case "${arg}" in
        --foo)
            arg__foo=true
            ;;
        --bar)
            arg__bar=true
            ;;
        -h|--help|*)
            print_usage
            ;;
    esac
    shift
done
