# task 4


class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = ""
        self.is_deleted = True

    def display(self, level=0):
        if self.is_deleted:
            printed_text = "Цей коментар було видалено."
        else:
            printed_text = f"{self.author}: {self.text}"
        print("\t" * level + printed_text)

        for reply in self.replies:
            reply.display(level + 1)


def main():
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    reply1_1_1 = Comment("Ти не правий, це шедевр!", "Олег")
    reply1_1_2 = Comment("Цілком погоджуюсь)", "Анонім")
    reply1_1.add_reply(reply1_1_1)
    reply1_1.add_reply(reply1_1_2)

    reply1_1_2.remove_reply()
    reply1.remove_reply()

    root_comment.display()


if __name__ == "__main__":
    main()
