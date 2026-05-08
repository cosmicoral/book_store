```mermaid
sequenceDiagram
    participant T as Terminal
    participant A as app.py
    participant R as AlbumRepository
    participant C as DatabaseConnection
    participant D as Database

    T->>A: python app.py
    A->>C: connect()
    A->>R: AlbumRepository(connection)
    A->>R: all()

    R->>C: execute("SELECT * FROM albums")
    C->>D: SELECT * FROM albums

    D-->>C: rows
    C-->>R: rows

    R-->>A: list of Album objects
    A-->>T: print albums
    