# Imports the module emoji for use in code
import emoji

# Gets command form the user to be converted into an emoji
command = input("Input: ")
emoji_command = emoji.emojize(command)
emoji_alias = emoji.emojize(command, language = "alias")
# Outputs user input converted into an emoji
if emoji_command != command:
    print(emoji_command)
else:
    print(emoji_alias)