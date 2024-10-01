def process_text(context):
    # Split the text into smaller chunks for embedding or processing
    chunks = []
    chunk_size = 400  # Set chunk size depending on needs
    for i in range(0, len(context), chunk_size):
        chunks.append(context[i:i + chunk_size])
    return chunks
