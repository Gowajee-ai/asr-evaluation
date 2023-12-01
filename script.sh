docker build -t gwj-evaluation:lastest . &&
docker run --name gowajee-evaluation -d -i -t gwj-evaluation:lastest &&
docker cp gowajee-evaluation:/results/result.csv ./results/result.csv &&
docker stop gowajee-evaluation &&
docker rm gowajee-evaluation &&
docker rmi $(docker images 'gwj-evaluation' -a -q)
