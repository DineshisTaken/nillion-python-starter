from nada_dsl import *

def create_magic_program():
    # Define mystical characters and parties
    seeker = Party(name="CodingSeeker")
    oracle = Party(name="TechOracle")
    alchemist = Party(name="InnovationAlchemist")
    decision_maker = Party(name="FinalJudge")

    # Secret evaluations from the mystical realms
    ancient_code = SecretInteger(Input(name="AncientCode", party=seeker))  # Previous score from ancient knowledge
    future_code = SecretInteger(Input(name="FutureCode", party=alchemist))  # New evaluation score with futuristic vision

    # Define the threshold for acceptance in the enchanted realm
    magical_threshold = SecretInteger(8)  # Adjust as per magical evaluation criteria

    # Initial decision based on the ancient knowledge
    initial_approval = ancient_code >= magical_threshold

    # Calculate the final score by combining ancient and future knowledge
    cosmic_balance = (ancient_code + future_code) / 2

    # Final decision based on the cosmic balance and threshold
    final_approval = cosmic_balance >= magical_threshold

    # Create an enchanting tale based on the final decision
    if final_approval:
        magical_story = (
            "In the mystical realms of coding, the CodingSeeker embarked on a quest through ancient texts "
            "and harnessed the wisdom of the TechOracle and the InnovationAlchemist. Together, they "
            "wove a spellbinding program that transcends time and space. This creation? A fusion of ancient "
            "lore and futuristic innovation, illuminating pathways to digital enlightenment. Under the gaze "
            "of the FinalJudge, they shape the future with every line of code!"
        )
    else:
        magical_story = (
            "Once upon a pixelated quest, the CodingSeeker ventured into the realm of code with a heart full "
            "of curiosity. Though ancient knowledge laid a foundation, it was the InnovationAlchemist who "
            "ignited the spark of creativity. They crafted a tale of resilience and growth, where every line "
            "of code echoed with potential. This journey? It’s not just about programs—it’s a testament to "
            "perseverance and the pursuit of magical mastery!"
        )

    return [
        Output(ancient_code, "AncientCode", party=decision_maker),
        Output(initial_approval, "InitialApproval", party=decision_maker),
        Output(future_code, "FutureCode", party=decision_maker),
        Output(cosmic_balance, "CosmicBalance", party=decision_maker),
        Output(final_approval, "FinalApproval", party=decision_maker),
        Output(magical_story, "MagicalStory", party=decision_maker)
    ]

if __name__ == "__main__":
    # Example input values for the enchanted demonstration
    Input.register("AncientCode", 7)    # Ancient code score
    Input.register("FutureCode", 9)     # New evaluation score with future vision

    # Cast the magic and create the program
    enchanted_outputs = create_magic_program()

    # Print enchanted outputs for review
    for output in enchanted_outputs:
        print(f"Enchanted Output {output.name} for {output.party.name}: {output.value}")
