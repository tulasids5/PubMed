import openai

def enhance_query_with_llm(query: str) -> str:
    prompt = f"Refine and optimize the following PubMed query: {query}. Make it more specific to biomedical research."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def is_pharma_biotech_affiliation(affiliation: str) -> bool:
    prompt = f"Is the following author affiliation related to pharmaceutical or biotech companies? {affiliation}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10
    )
    return "yes" in response.choices[0].text.lower()