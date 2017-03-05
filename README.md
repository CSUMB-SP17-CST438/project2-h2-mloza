# project2-h2-mloza

## Theme 
Food

## How did you incorporate your theme within your project?
The background image is sushi and the API that Dragon-bot calls is Yelp for food places.

## Problems?
The biggest two problems were Yelp and CircleCl.

I had issues setting up the OAuth for Yelp. I was following the setup from Facebook. It
wasn't working. I looked around and tried a few but kept getting wrong setup erros. I 
eventually tried Facebook's OAuth again. It works. I'm pretty sure it's because I copied
the wrong key to the wrong spot.

CircleCl didn't like my socketio tests. It had issues connecting to my database. Someone
from Slack suggested to add an enviroment variable in CircleCl for Heroku db. It now works,
which makes sense. Lastly, integrations tests wouldn't allowing CircleCl to build. However,
I finally realized that it was because that I forgot the - at the beginning. 

## How would you improve it if you had more time?
I would try to figure out how to only have the login buttons if the client hasn't
logged in. If they are, then only show their associated logout button. But I
can't seem to figure it out.

## Points from handin 1
I managed to get google login working. However, it is advised to logout from
Facebook before logging in and vice versa.