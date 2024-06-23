export const invoke = (
    action: string,
    version: number = 6,
    params: object = {}
) => {
    return new Promise(async (resolve, reject) => {
        try {
            const response = await fetch("http://127.0.0.1:8765", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    action,
                    version,
                    params,
                }),
            });

            if (!response.ok) {
                throw "failed to issue request";
            }

            const jsonResponse = await response.json();

            if (Object.getOwnPropertyNames(jsonResponse).length != 2) {
                throw "response has an unexpected number of fields";
            }
            if (!jsonResponse.hasOwnProperty("error")) {
                throw "response is missing required error field";
            }
            if (!jsonResponse.hasOwnProperty("result")) {
                throw "response is missing required result field";
            }
            if (jsonResponse.error) {
                throw jsonResponse.error;
            }

            resolve(jsonResponse.result);
        } catch (e) {
            reject(e);
        }
    });
};

export const fetchCardsInfo = async () => {
    const current_deck = { name: "CalHacks", id: 1719082606356 };

    const cardList = (await invoke("findCards", 6, {
        query: `deck:${current_deck.name}`,
    })) as string[];

    const dueCards = (await invoke("areDue", 6, {
        cards: cardList,
    })) as boolean[];

    const dueCardList = cardList.filter((_, i) => dueCards[i]) as string[];

    const cardInfo = (await invoke("cardsInfo", 6, {
        cards: dueCardList,
    })) as any[];

    return cardInfo.map((card) => {
        return {
            id: card.cardId,
            question: card.fields.Question.value,
            answer: card.fields.Answer.value,
        };
    });
};

export const answerCard = async (cardId: string, ease: string) => {
    await invoke("answerCard", 6, {
        cardId: parseInt(cardId),
        ease: parseInt(ease),
    });
};
