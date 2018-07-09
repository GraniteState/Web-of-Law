from utils import *


class ModelBiRNN(nn.Module):
    def __init__(self, params, embeddings):
        super(ModelBiRNN, self).__init__()
        self.l_emb = embeddings['src']
        self.l_birnn = GRUBiRNN(params['dim_emb'], params['dim_hid'], params['num_rnn_layer'])
        self.l_ff = nn.Sequential(
            torch.nn.Linear(2 * params['dim_hid'], params['dim_hid']),
            torch.nn.Dropout(params['dropout']),
            torch.nn.ReLU()
        )
        self.l_out = nn.Sequential(
            torch.nn.Linear(params['dim_hid'], params['n_classes']),
            torch.nn.LogSoftmax(1)
        )

    def forward(self, x):
        x, seq_lens = self.l_emb(x['src'])
        x = self.l_birnn(x, seq_lens)
        x = self.l_ff(x)
        x = self.l_out(x)
        return x