from storage import VectorStore, MemoryStore

# Test vector storage
vector = VectorStore()
chunks = [
    {"text": "CHEM 101 Lab Report 1 due Friday Jan 30 at 5pm", "metadata": {"course_id": "chem101", "week": 2, "type": "assignment"}},
    {"text": "PHYS 202 Midterm covers chapters 1-4", "metadata": {"course_id": "phys202", "week": 6, "type": "exam"}}
]

print("🧪 Storing chunks...")
vector.store_chunks("chem101", chunks[:1])
vector.store_chunks("phys202", chunks[1:])

print("\n🔍 Retrieving from CHEM 101...")
results = vector.retrieve_chunks("chem101", "lab report due date")
for r in results:
    print(f"Text: {r['text'][:50]}...")
    print(f"Metadata: {r['metadata']}")

# Test memory storage  
memory = MemoryStore()
print("\n🧠 Storing student memory...")

memory.append_memory(
    user_id="student123",
    memory_type="chat_summary",
    course_id="chem101",
    payload={
        "summary": "Student asked about lab due dates, created study plan for Friday"
    },
)

print("\n📚 Recent memory:")
recent = memory.get_recent_memory("student123")
for item in recent:
    print(f"Type: {item['type']}, Course: {item['course_id']}")
    print(f"Payload: {item['payload']}")


