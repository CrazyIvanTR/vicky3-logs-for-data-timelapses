Open powershell (win -> powershell).

Go to the logs folder, default is:

```cd '.\Documents\Paradox Interactive\Victoria 3\logs\'```

Run command:

```Get-Content debug.log -Wait | Out-File -FilePath "00-full-debug.txt" -Append```

Run the game with the mod here: https://steamcommunity.com/sharedfiles/filedetails/?id=3713168053

All the logs that are put inside debug.log will also be put inside 00-full-debug.txt

Install python, I tested on 3.14, should work with almost any version since it's pretty basic code.

Download this as a zip and extract to logs folder to run more easily. I used that exact method, just made the files under there and copied them over to the repo.

Some lines will be duplicates, to check for duplicates run `py check_for_duplicates_in_original.py` to check 00-full-debug.txt

Run the file `py remove_duplicates.py` to remove duplicates from 00-full-debug.txt and write to 00-full-debug-deduplicated.txt

Run the file `py check_for_duplicates_in_deduplicated.py` to check if there are still duplicates (if there are, which there shouldn't be, rename the file to 00-full-debug.txt and try again ?)

-------------------------

Not sure if the deduplication will work with files at 700MB size but it should unless you run out of RAM.

I can only guarantee that there's nothing malicious in the code (it reads file, puts it into a set, finds duplicates and either prints them or removes them and prints to a new file, that's all)

You can open an issue to ask stuff or give suggestions or just open a PR for a better version, I'm not really planning on maintaining this.
