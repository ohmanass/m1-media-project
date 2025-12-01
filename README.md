# 🎬 MediaProject

**👤 Author:** Nassim TOUISSI – M1 Dev&Data Student at H3 Hitema

## 🌟 Overview

MediaProject is a Django REST Framework backend for media ingestion and management.  
It allows authenticated users to upload videos and miniatures, store them on a CDN, manage metadata, and expose them through a REST API. The system uses PostgreSQL, MongoDB, Redis, JWT, and async workers, and is containerized with Docker.

---

## 📝 Requirements

The system must:

- ✅ Provide full CRUD on media resources  
- 🐘 Use PostgreSQL for core entities (users, roles, media, jobs, URL, miniature) with ORM  
- 🍃 Use MongoDB for detailed technical metadata with ODM  
- 🔁 Use Redis for caching and deduplication (avoid duplicate uploads)  
- ⚡ Use background tasks and Redis for async processing (CDN upload + metadata retrieval)  
- 🔒 Protect the API with JWT middleware  
- 👑 Offer an admin mode to manage users and roles  
- 🐳 Be containerized with Docker and covered by unit tests (~80%)  

---

## 🧑‍💻 Roles

- **Admin** – full access, manage users and roles  
- **Media Operator** – upload media, manage own media, view job status  
- **Viewer** – read-only access  

---

## 📡 Core Endpoints

- `GET /ping/` – return 🏓 pong  
- `GET /version/` – return 🆚 version  
- `POST /auth/signup/` – create 👤 user  
- `POST /auth/signin/` – get 🔑 JWT  
- `POST /media/` – create 🎥 media (video + miniature), dedup with Redis, enqueue job  
- `GET /media/` – list 📄 media with pagination  
- `GET /media/{uuid}/` – media details 🔍  
- `PATCH /media/{uuid}/` – update media ✏️ (role-based)  
- `DELETE /media/{uuid}/` – delete media 🗑️ (role-based)  
- `GET /media/{uuid}/jobs/` – job history 📊  
- `GET /search?title=...` – title search 🔎 (Redis + DB)  

---

## ⚡ Async Processing

- `upload_to_cdn(media_id)` – upload media to CDN, update status ☁️  
- `extract_metadata(media_id)` – extract metadata and store in MongoDB 🗂️  

---

## 🔐 Security

- JWT middleware + DRF authentication & permission classes 🔑  
- Validation using **Pydantic** 🛡️  

---

## 🏗️ Architecture

- Django backend (port 8000) 🖥️  
- PostgreSQL (port 5432) 🐘  
- MongoDB (port 27017) 🍃  
- Redis (port 6379) 🔁  
- Async workers via Redis ⚡  
- Dockerized with docker-compose 🐳  

---

## 🧪 Testing

- JWT auth, role-based permissions 🔑  
- Redis deduplication logic 🔁  
- Async status updates ⚡  
- PostgreSQL/MongoDB consistency 🗃️  

---

## 📬 Postman

- Add a Postman collection to automate API calls 📨  

---

## 📝 Notes / Conventions

- English names for all functions, classes, variables, files ✍️  
- PEP8 style (use black) 🖤  
- Clean architecture, OOP only 🏛️  
- Short functions, clear responsibilities ✂️  
- Atomic commits 💾
