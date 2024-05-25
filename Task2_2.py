# Lesson 2: Tuples
# 2. Python Data Structure Challenges in Real-World Scenarios

def add_book(library, title, author):
    new_book = (title, author)
    if new_book in library:
        print(f"Book '{title}' by {author} already exists in the library.")
    else:
        library.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
add_book(library, "To Kill a Mockingbird", "Harper Lee")
add_book(library, "1984", "George Orwell")
add_book(library, "The Great Gatsby", "F. Scott Fitzgerald")

print("\nUpdated Library:")
for i, (title, author) in enumerate(library, start=1):
    print(f"{i}. {title} by {author}")
