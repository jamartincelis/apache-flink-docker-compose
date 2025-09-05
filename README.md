# Apache Flink Docker Compose

_Proyecto que pretende mostrar el uso de apache flink mediente docker compose_

# Iniciar el cluster
```bash
docker-compose up -d
```

# Escalar taskmanagers
```bash
docker-compose up -d --scale taskmanager=3
```

# Ver logs
```bash
docker-compose logs -f
```

# Ejecutar un job
```bash
docker-compose exec python-client python3 jobs/word_count.py
```

# Acceder a la interfaz web
**[Apache Flink Dashboard](http://localhost:8081)** (para gestionar flink).
# 

# Detener el cluster
```bash
docker-compose down
```
