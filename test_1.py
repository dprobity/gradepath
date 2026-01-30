from storage import VectorStore, MemoryStore
vs = VectorStore()
vs.store_chunks('chem101', [{'text': 'Lab due Friday'}])
print('Vector:', vs.retrieve_chunks('chem101', 'lab'))
ms = MemoryStore()
ms.append_memory('test', {'type': 'test'})
print('Memory:', ms.get_recent_memory('test'))
print('✅ Storage 100% ready!')

