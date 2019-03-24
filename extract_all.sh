#!/usr/bin/env bash

# Dark Background Hymns
python3 extract.py hymns/hymns processed_hymns/dark/hymns/43_normal backgrounds/white_text white normal
python3 extract.py hymns/hymns processed_hymns/dark/hymns/169_wide backgrounds/white_text white wide

# Dark Background Other Songs
python3 extract.py hymns/other_songs processed_hymns/dark/other_songs/43_normal backgrounds/white_text white normal
python3 extract.py hymns/other_songs processed_hymns/dark/other_songs/169_wide backgrounds/white_text white wide

# Bright Background Hymns
python3 extract.py hymns/hymns processed_hymns/bright/hymns/43_normal backgrounds/black_text black normal
python3 extract.py hymns/hymns processed_hymns/bright/hymns/169_wide backgrounds/black_text black wide

# Bright Background Other Songs
python3 extract.py hymns/other_songs processed_hymns/bright/other_songs/43_normal backgrounds/black_text black normal
python3 extract.py hymns/other_songs processed_hymns/bright/other_songs/169_wide backgrounds/black_text black wide