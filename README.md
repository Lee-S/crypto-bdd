# crypto-bdd
###An exercise in testing APIs using BDD.

A crypto client was developed to be used by the BDD features.  Some pyest unittests exist for a few parts of this.
pytest-tdd library was used to write BDD feature files for public and private API tests, along with thier step implementation.


1. Checkout repo
`git clone https://github.com/Lee-S/crypto-bdd.git`

2. Create a .env file in the root of the project.  This contains secrets that are not committed to github
```
API_URL="https://api.EXCHANGE.com/"
API_KEY="XYZ123ABC"
PVT_KEY="XYZ123ABC"
KEY_2FA="ABCABC"
```

3. Build the Docker image
`docker build -t bdd_image .`

4. Run the container
``

5. Navigate to the url shown where you will see a html report of test results.
