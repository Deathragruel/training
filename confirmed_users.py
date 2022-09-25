# Start with users that need to be verified,
# and an empty list for confirmed users.
unconfirmed_users = ['candace', 'alice', 'brian']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each unconfirmed user to the list of confirmed users
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f"Verifying {current_user.title()}.")
	confirmed_users.append(current_user)
# Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())