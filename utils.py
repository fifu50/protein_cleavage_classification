# Useful functions for the project

def _open_file_(filename, str_detailed=False, masked=False):
    """
    # Input:

    Returns data from file (private function)
    """
    euk_sig = []
    str_details = None
    if str_detailed:
        str_details = []
    mask = None
    if masked:
        mask = []

    with open(filename, 'r') as f:
        for ind, line in enumerate(f):
            if ind % 3 == 1:
                euk_sig.append(line.strip())
            elif str_detailed and ind % 3 == 0:
                str_details.append(line.strip())
            elif masked and ind % 3 == 2:
                mask.append(line.strip())

    return euk_sig, str_details, mask


def get_euksig(str_detailed=False, masked=False):
    return _open_file_('data/EUKSIG_13.red', str_detailed=str_detailed, masked=masked)


def get_gram_neg(str_detailed=False, masked=False):
    return _open_file_('data/GRAM-SIG_13.red', str_detailed=str_detailed, masked=masked)


def get_gram_pos(str_detailed=False, masked=False):
    return _open_file_('data/GRAM+SIG_13.red', str_detailed=str_detailed, masked=masked)
