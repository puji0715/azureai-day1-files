# 4. Use AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-12-01-preview"  # Use a recent stable API version
)

# 5. Call the model (model parameter uses deployment name)
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a named entity recognition assistant. Extract all person names, organization names, and locations from the user's text, and return them in JSON format with keys 'persons', 'organizations', 'locations'."},
        {"role": "user", "content": "Satya Nadella, CEO of Microsoft, announced a new partnership with the University of Washington in Seattle."}
    ]
)

print(response.choices[0].message.content)
