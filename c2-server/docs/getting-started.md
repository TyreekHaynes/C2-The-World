# Getting Started with C2 Framework

## Quick Start (5 minutes)

### Prerequisites
- Docker and Docker Compose
- Python 3.9+ (for agent development)
- Git

### Option 1: Docker Deployment (Easiest)


# Clone the repository
git clone https://github.com/TyreekHaynes/c2-framework.git
cd c2-framework

# Generate a master key
export C2_MASTER_KEY=$(python -c "from cryptography.fernet import Fernet; import base64; print(base64.b64encode(Fernet.generate_key()).decode())")

# Start everything
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
