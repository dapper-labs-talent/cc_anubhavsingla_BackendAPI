How long did this assignment take?
> About 6 hours

What was the hardest part?
> A lot of time to setup the infra, e.g. PostgreSQL server.

> Attempt the assignment in time constraint, was hard to prioritize the aspects of assignment to focus on without much evaluation guildlines.

Did you learn anything new?
> Yes, good learning excersize. I haven't done a lot of infra setup from scratch. 

Is there anything you would have liked to implement but didn't have the time to?

> User input validation, instead of assuming the incoming request payload to have right set of keys and length of value strings.

> Appropriate error codes being returned from backend, instead of defaults due to exceptions

> A good suite of unit-tests at the client which includes more test cases and error scenarios. Maybe unittests for backend.

> An API to delete the entries at the backend, to help with testing. 

> Containerize the flask app and the test client. Remove need for most lines in `INSTRUCTIONS.md` file

What are the security holes (if any) in your system? If there are any, how would you fix them?
> `SECRET` for JWT is part of code in plain text. This can be instead derived crypto randomely generated when the server starts. Or derived from the existing user/machine certificates.

> User password is being stored in plaintext in the database. It should be crypto salted+hashed before being stored. Password plain text should not be a part of JWT payload.

> Database password is being stored in plaintext in code. User/machine certificates can be used for sophisticated access control.

> JWT should be generated with expiration time. It is a simple fix, supported by by the standard. Current system compromises a user forever once JWT is exposed.

> User input should be validated on the backend for any unexpected script injections.

Do you feel that your skills were well tested?
> Getting my skills well tested is not important for me. Over the years, I have acquired diverse but niche set of skill which may not be relevant everywhere.