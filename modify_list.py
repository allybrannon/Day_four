# han_description = ['stuck-up', 'half-witted', 'scruffy-looking', 'nerf-herder']
# print(han_description)

# han_description[2] = "Who's Scruffy Looking?"
# han_description[3] = "Master Pilot"

# print(han_description)

falcon_parts = ["Toplex Deflector Shield", "L3 + V-5 Navigation",
                "SSP05 Hyperdrive", "AG-2G Laser Cannon", "Escape Pod"]
# # print(falcon_parts)

# hans_modifications = ["L3 + V5 Navgation", "SSP05 Hyperdrive"]

# falcon_parts[1] = hans_modifications
# print(falcon_parts)

# falcon_parts.append("AG-2G Laser Cannon")
# print(falcon_parts)

# falcon_parts.extend(["sensor Proof Smuggler Compartment",
#                      "Aurodium-Plated Gold Dice"])
# print(falcon_parts)

# inserting, not deleting
# falcon_parts.insert(0, "Dejarik Board")
# print(falcon_parts)

# poorly_cloned_falcon = falcon_parts + ["Wookie"]
# print(falcon_parts)
# print(poorly_cloned_falcon)

# pop without any argument removes the last item!
removed_part = falcon_parts.pop(3)
print(removed_part)
print(falcon_parts)
