# crypto-bdd
An exercise in BDD

1. Checkout repo
`git clone https://github.com/Lee-S/crypto-bdd.git`

2. Create a .env file in the root of the project.  This contains secrets that are not committed to github
```
API_URL="https://api.EXCHANGE.com/"
API_KEY="XYZ"
PVT_KEY="ABC"
KEY_2FA="123"
```

3. Build the Docker image
`docker build -t bdd_image .`

4. Run the container
``

5. Navigate to the url shown where you will see a html report of test results.
