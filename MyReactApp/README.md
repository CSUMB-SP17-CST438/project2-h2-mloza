# lecture7-thuhe

Wiring Flask with Socket.io: a review

## Upgrade Node version to 6

```$ nvm install 6```

## Installing Webpack globally

This line installs Webpack on your Cloud9 workspace, kind of like how you might
install from a package or `brew install` something.

```$ npm install -g webpack```

## Installing `npm` dependencies from `package.json`

This line starts up `npm`, which looks inside `package.json`, gets a list of
packages, and installs them to the `node_modules` folder inside your repository.

```$ npm install```

## Compiling Javascript using Webpack

This line starts up Webpack, which looks inside `webpack.config.js`, loads
configuration options, and starts transpiling your JS code into `static/script.js`.

```$ webpack --watch```

(The program should not stop running. Leave it running.)

## Edit a JS file

Make a change to `scripts/Content.js`. Webpack should detect the change and
print a bunch of stuff.

**Do not manually edit `static/script.js`!!**

## Run the web app

Run `app.py` and verify that the React renders. Click on "Send up a random
number". What gets printed out in the logs?

## Make the web page interactive!

Your goal is to build an app that that will update live with a new random number whenever
the you click on "Send up a random number". The client is completely done for you:

* `Button.js` contains code for the button, generating a random number, and
sending it up to the server.
* `Content.js` contains code for taking a list of numbers from the server, and
rendering it as a list in React.

You'll need to fill out the server-side portion. I've left a TODO in the code
starting point. You'll want to:

* Keep track of the list of numbers you're getting
* Update that list internally when clients send you a new number
* Send the new list out to clients when you're done

## Answer this conceputal question:

How do I get the list to clear?

## Finished?

Try to add these:

* Make the server send the list when the client connects
* Add a button that clears the list
