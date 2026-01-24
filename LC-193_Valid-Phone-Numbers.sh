# Problem: LC 193. Valid Phone Numbers
# Solution from: Loginov Kirill
# Solution link: https://leetcode.com/problems/valid-phone-numbers/solutions/6627001/master-regex-filtering-unlock-the-power-ggz6v/

# Read from the file file.txt and output all valid phone numbers to stdout.
grep -E '^((\([0-9]{3}\) [0-9]{3}-[0-9]{4})|([0-9]{3}-[0-9]{3}-[0-9]{4}))$' file.txt
#grep -E ' ^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt
