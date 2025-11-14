import random

responses = [
    "✨ Absolutely yes!",
    "🤔 Hmm... maybe.",
    "😬 Probably not.",
    "🌈 Without a doubt!",
    "💫 Ask again later.",
    "❌ No chance!",
    "🌻 100% yes!",
    "🌙 The stars say... yes."
]

question = input("Ask the Magic 8-Ball a yes/no question: ")
print("\n🔮 The Magic 8-Ball says:", random.choice(responses))

#write any question in the INPUT and let the magic 8 ball answer your question <3
