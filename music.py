
_get_repolink () {
    local regex
    regex='(https?)://github.com/.+/.+'
    if [[ $LEGEND_REPO == "LEGENDBOT" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL0xFR0VORC1PUy9NVVNJQy1WQy9hcmNoaXZlL21haW4uemlw" | base64 -d
    elif [[ $LEGEND_REPO == "LEGENDBOT" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL0xFR0VORC1PUy9NVVNJQy1WQy9hcmNoaXZlL21haW4uemlw" | base64 -d
    elif [[ $LEGEND_REPO =~ $regex ]]
    then
        if [[ $LEGEND_REPO_BRANCH ]]
        then
            echo "${LEGEND_REPO}/archive/${LEGEND_REPO_BRANCH}.zip"
        else
            echo "${LEGEND_REPO}/archive/master.zip"
        fi
    else
        echo "aHR0cHM6Ly9naXRodWIuY29tL0xFR0VORC1PUy9NVVNJQy1WQy9hcmNoaXZlL21haW4uemlw" | base64 -d
    fi
}


_setting_bot () {
    local zippath
    zippath="music.zip"
    echo "  Downloading LegendBot V3.O Source Code..."
    wget -q $(_get_repolink) -O "$zippath"
    echo "  Unpacking Data ..."
    LEGENDPATH=$(zipinfo -1 "$zippath" | grep -v "/.");
    unzip -qq "$zippath"
    echo "Done"
    echo "  LegendBot V3.O Cleaning.."
    rm -rf "$zippath"
    sleep 5
    cd $LEGENDPATH
    echo "    ⚜️Starting Lêɠêɳ̃dẞø†⚜️     "
    echo "
    🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳
    "

    python3 ../setup/updater.py ../requirements.txt requirements.txt
    python3 main.py
}

_setting_bot