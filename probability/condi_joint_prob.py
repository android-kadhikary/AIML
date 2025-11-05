import sympy as sp

#prob of draw number 5 in a single dice

prob_num6_single_dice= sp.Rational(1,6)

#prob of both draw  6 in 2 dices
Total_prob_both_dice_6=prob_num6_single_dice*prob_num6_single_dice
print (f"Total_prob_both_dice_6 (A intersection B) = {Total_prob_both_dice_6}")

#cards draw
king_whwnGivenFaceCard_P= sp.Rational(4,12)
face_card_P=sp.Rational(12,52)
P_of_FaceAndKing=face_card_P*king_whwnGivenFaceCard_P
print("P_of_FaceAndKing = ",P_of_FaceAndKing)