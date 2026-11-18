import json
import os


JSON_DIR = "preprocessing/dataset_json"


def load_json(name):
    path = os.path.join(JSON_DIR, name + ".json")
    with open(path, "r") as f:
        return json.load(f)[name]


def save_json(name, data):
    path = os.path.join(JSON_DIR, name + ".json")
    with open(path, "w") as f:
        json.dump({name: data}, f, indent=2)
    print(f"Created {path}")


def combine(name, files):
    combined = {
        "real": {
            "test": {}
        },
        "fake": {
            "test": {}
        }
    }

    for file in files:
        dataset = load_json(file)

        combined["real"]["test"].update(
            dataset.get("real", {}).get("test", {})
        )

        combined["fake"]["test"].update(
            dataset.get("fake", {}).get("test", {})
        )

    save_json(name, combined)

    print(
        f"  Real videos: {len(combined['real']['test'])}\n"
        f"  Fake videos: {len(combined['fake']['test'])}"
    )


# -------------------------
# Source-based combinations
# -------------------------

combine(
    "DF40_TEST_cdf",
    [
        "DF40_TEST_real_cdf",
        "DF40_TEST_EFS_cdf",
        "DF40_TEST_FE_cdf",
        "DF40_TEST_FR_cdf",
        "DF40_TEST_FS_cdf",
    ]
)


combine(
    "DF40_TEST_ff",
    [
        "DF40_TEST_real_ff",
        "DF40_TEST_EFS_ff",
        "DF40_TEST_FE_ff",
        "DF40_TEST_FR_ff",
        "DF40_TEST_FS_ff",
    ]
)


combine(
    "DF40_TEST_other",
    [
        "DF40_TEST_real_other",
        "DF40_TEST_EFS_other",
        "DF40_TEST_FE_other",
        "DF40_TEST_FR_other",
        "DF40_TEST_FS_other",
    ]
)


# -------------------------
# Manipulation-based combinations
# -------------------------

real_sets = [
    "DF40_TEST_real_cdf",
    "DF40_TEST_real_cdfv1",
    "DF40_TEST_real_ff",
    "DF40_TEST_real_other",
]


for manipulation in ["EFS", "FE", "FR", "FS"]:

    combine(
        f"DF40_TEST_{manipulation}",
        real_sets +
        [
            f"DF40_TEST_{manipulation}_cdf",
            f"DF40_TEST_{manipulation}_ff",
            f"DF40_TEST_{manipulation}_other",
        ]
    )


# -------------------------
# Full DF40
# -------------------------

combine(
    "DF40_TEST_all",
    [
        "DF40_TEST_real_cdf",
        "DF40_TEST_real_cdfv1",
        "DF40_TEST_real_ff",
        "DF40_TEST_real_other",

        "DF40_TEST_EFS_cdf",
        "DF40_TEST_EFS_ff",
        "DF40_TEST_EFS_other",

        "DF40_TEST_FE_cdf",
        "DF40_TEST_FE_ff",
        "DF40_TEST_FE_other",

        "DF40_TEST_FR_cdf",
        "DF40_TEST_FR_ff",
        "DF40_TEST_FR_other",

        "DF40_TEST_FS_cdf",
        "DF40_TEST_FS_ff",
        "DF40_TEST_FS_other",
    ]
)
