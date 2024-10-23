def sum_nested_list(lst):
    total_size = 0
    for f in lst:
        if isinstance(f, int):
            total_size += f
        else:
            total_size += sum_nested_list(f)

    return total_size


dirs = {
    "Documents": {
        "Proposal.docx": None,
        "Receipts": {
            "January": {"receipt1.txt": None, "receipt2.txt": None},
            "February": {"receipt3.txt": None},
        },
    },
}


def list_files(current_filetree, current_path=""):
    file_paths = []
    for node, value in current_filetree.items():
        if value is None:
            file_paths.append(current_path + "/" + node)
        else:
            file_paths += list_files(value, current_path + "/" + node)

    return file_paths


nested_levels = {1: {3: {4: {}}}, 2: {}}


def count_nested_levels(nested_documents, target_document_id, level=1):
    for document_id in nested_documents:
        if document_id == target_document_id:
            return level
        else:
            found_level = count_nested_levels(
                nested_documents[document_id], target_document_id, level + 1
            )
            if found_level != -1:
                return found_level
    return -1


def reverse_string(s):
    if not s:
        return ""
    reversed = s[-1] + reverse_string(s[:-1])

    return reversed


def find_longest_word(document, longest_word=""):
    if not document:
        return longest_word
    word, *document = document.split(" ")
    document = " ".join(document)

    if len(word) > len(longest_word):
        longest_word = word

    longest_word = find_longest_word(document, longest_word)

    return longest_word
