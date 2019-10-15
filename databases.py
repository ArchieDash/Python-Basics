import sqlite3


with sqlite3.connect(":memory:") as connection:
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Roster(
        Name TEXT,
        Species TEXT,
        IQ INT
        );"""
    )
    data = (
        ("Jean-Baptiste Zorg", "Human", 122),
        ("Korben Dallas", "Meat Popsicle", 100),
        ("Ak'not", "Mangalore", -5)
            )
    cursor.executemany(
        """INSERT INTO Roster VALUES(?, ?, ?);""", data
    )
    cursor.execute("UPDATE Roster SET Species='Human' WHERE NAME='Korben Dallas'")
    cursor.execute(
        """SELECT Name, IQ FROM Roster
            WHERE Species='Human';
        """
    )
    for row in cursor.fetchall():
        print(row)
